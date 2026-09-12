"""PPix Photo-thumb."""

from app.library_walk import collect_library_items as _collect


def _install() -> None:
    from app.plex_api import PlexClient, PlexError

    def _page(self, path, params, start, size):
        q = dict(params or {})
        q["X-Plex-Container-Start"] = str(start)
        q["X-Plex-Container-Size"] = str(size)
        return self._xml(
            "GET",
            path,
            params=q,
            extra_headers={
                "X-Plex-Container-Start": str(start),
                "X-Plex-Container-Size": str(size),
            },
        )

    _orig_parse = PlexClient._parse_item

    def _parse_item(self, node, section_key):
        if getattr(node, "tag", "") == "Directory":
            return None
        return _orig_parse(self, node, section_key)

    def _collect_items(self, section_key, include_videos=True, cancel_cb=None, progress_cb=None):
        return _collect(self, section_key, include_videos, cancel_cb, progress_cb)

    def clear_item_thumb(self, rating_key: str) -> None:
        if not rating_key:
            return
        for kind in ("posters", "arts"):
            try:
                root = self._xml("GET", f"/library/metadata/{rating_key}/{kind}")
            except Exception:
                continue
            for node in list(root):
                url = node.attrib.get("key") or node.attrib.get("ratingKey") or ""
                if not url:
                    continue
                try:
                    self._request(
                        "DELETE",
                        f"/library/metadata/{rating_key}/{kind}",
                        params={"url": url},
                    )
                except PlexError:
                    continue
        try:
            self._request(
                "PUT",
                f"/library/metadata/{rating_key}",
                params={"thumb.locked": "0", "thumb": ""},
            )
        except PlexError:
            pass

    PlexClient._page = _page
    PlexClient._parse_item = _parse_item
    PlexClient.collect_library_items = _collect_items
    PlexClient.clear_item_thumb = clear_item_thumb


_install()
