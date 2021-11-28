def make_album(s_name, a_name):
    describe_album = {}
    describe_album["singer_name"] = s_name
    describe_album['album_name'] = a_name
    return describe_album

da_name = make_album('周杰伦','摩羯座')
print(da_name)

