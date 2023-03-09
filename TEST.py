from pgboost import *

InitSettings.Change(skyboxValue=(20,20,20),sizes=(1200,750))
Application.Init()

class MyGame(Game):
    class MySprite(Sprite):
        def __init__(self,sprite,rect) -> None:
            super().__init__()
            self.image = sprite
            self.rect = rect
            self.realpos = self.rect.center
            
        def update(self ):
            self.rect.center = Camera.Project(self.realpos)
    
    def Start(self):
        
        s = {
            "font_name":"Segoe UI",
            "font_size":FS_BIG
        }
        
        m = UI.AddManager(UIManager(InitSettings.sizes,default_settings_override=s),True)
        self.l = UILabel(Rect(Window.center.x-200,20,400,50),m,"FPS: 60")
        self.s = SpriteManager.Add("player","assets/test/goldenjerold.png",(0.2,0.2))
        
        self.group = SpriteGroup()
    
    def Update(self):
        Camera.Drag([1,2])
        val = Camera.Zoom()
        if val:
            sc = Camera.ZoomSurface(self.s)
            for s in self.group:
                s.image = sc
                s.rect = s.image.get_rect(center = s.rect.center)
        
        if Input.GetMouse(0):
            new = MyGame.MySprite(self.s,self.s.get_rect(center=Camera.ScreenToWorld(Input.mousePosition)))
            new.image = Camera.ZoomSurface(self.s)
            self.group.add(new)
        
        self.group.update()
                
        self.l.set_text(f"FPS: {Math.Round(Time.frameRate,2)}, Sprites: {len(self.group.sprites())}")
        
    def Draw(self):
        self.group.draw(Window.surface)

Application.Run(MyGame())