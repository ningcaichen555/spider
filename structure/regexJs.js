function f() {
    var reg = '^< img.*src=\\"(.*)\\".*/>$'
    var str = '< img src="1a66ece32e827c62cc748c6a13ce2afb.jpg"'
    str.replace(reg, '$1-fsdfsd')
}

f()