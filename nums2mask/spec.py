def parse_mask_spec(value: str) -> dict[str, list[int]]:
    values = value.split()
    if len(values) == 1:
        return {'': _csv2list(values[0])}
    return dict(map(_parse_kv, values))


def _parse_kv(kv: str) -> tuple[str, list[int]]:
    try:
        key, value = kv.split(':')
    except ValueError:
        raise ValueError(f'"{kv} contains more than one ":"')
    return key, _csv2list(value)


def _csv2list(s: str) -> list[int]:
    try:
        return [int(v.strip()) for v in s.split(',')]
    except ValueError:
        raise ValueError(f'{s} is not a CSV of integers')


assert parse_mask_spec('lh.wm.mnc:160,4 rh.wm.mnc:161,5') == {'lh.wm.mnc': [160, 4], 'rh.wm.mnc': [161, 5]}
assert parse_mask_spec('161,5') == {'': [161, 5]}
