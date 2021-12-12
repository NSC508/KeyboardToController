class controller:
    MAX_VJOY = 32767
    self.joystick = pyvjoy.VJoyDevice(1)

    def play_function(self,X,Y,Z,XRot):
        self.joystick.data.wAxisX = int(X * self.MAX_VJOY)
        self.joystick.data.wAxisY = int(Y * self.MAX_VJOY)
        self.joystick.data.wAxisZ = int(Z * self.MAX_VJOY)
        self.joystick.data.wAxisXRot = int(XRot * self.MAX_VJOY)
        joystick.update()