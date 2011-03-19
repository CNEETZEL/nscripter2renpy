init 1:
  transform right2:
    xalign 1.33

  transform left2:
    xalign -0.03

  python:
    menu = nvl_menu
    narrator = Character(None, kind=nvl)
    autoclick = 3600

    def scale(img):
      print(img)
      (w, h) = Image(img).load().get_size()
      rw = config.screen_width / float(w)
      rh = config.screen_height / float(h)
      return im.FactorScale(img, rw, rh)
  
    def alpha_blend(img):
      (w, h) = Image(img).load().get_size()
      rh = config.screen_height / float(h)
      i = im.Crop(img, (0, 0, w/2, h))
      m = im.MatrixColor(im.Crop(img, (w/2, 0, w/2, h)), im.matrix.invert())
      return im.FactorScale(im.AlphaMask(i, m), rh, rh)