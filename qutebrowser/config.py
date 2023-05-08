import dracula.draw

# Load existing settings made via :set
config.load_autoconfig()

dracula.draw.blood(c, {
    'spacing': {
        'vertical': 6,
        'horizontal': 8
    }
})
c.url.start_pages = ["https://duckduckgo.com/?k7=282a36&k8=f8f8f2&k9=50fa7b&kae=t&kt=p&ks=m&kw=n&km=l&ko=s&kj=282a36&ka=p&kaa=bd93f9&ku=-1&kx=f1fa8c&ky=44475a&kaf=1&kai=1&kf=1/"]
c.session.default_name = "havan"
c.auto_save.session = True
c.confirm_quit = ['always']
