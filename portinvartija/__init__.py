# [[[fill git_describe()]]]
__version__ = '2023.10.29+parent.e53151b0'
# [[[end]]] (checksum: 065626152e6d0d8e21024deba1bbba5b)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
