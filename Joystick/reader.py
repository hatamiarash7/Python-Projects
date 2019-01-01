import pygame
import serial

usb = serial.Serial('COM3', 9600, timeout=None, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
command = ""


class TextPrint:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        self.font = pygame.font.Font(None, 20)

    def print(self, my_screen, text_string):
        text_bitmap = self.font.render(text_string, True, BLACK)
        my_screen.blit(text_bitmap, [self.x, self.y])
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def un_indent(self):
        self.x -= 10


pygame.init()
size = [500, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
done = False
clock = pygame.time.Clock()
pygame.joystick.init()
textPrint = TextPrint()

while done is False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released")

    screen.fill(WHITE)
    textPrint.reset()
    joystick_count = pygame.joystick.get_count()
    textPrint.print(screen, "Number of joysticks: {}".format(joystick_count))
    textPrint.indent()

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        textPrint.print(screen, "Joystick {}".format(i))
        textPrint.indent()

        name = joystick.get_name()
        textPrint.print(screen, "Joystick name: {}".format(name))

        axes = joystick.get_numaxes()
        textPrint.print(screen, "Number of axes: {}".format(axes))
        textPrint.indent()

        for j in range(axes):
            axis = joystick.get_axis(j)
            textPrint.print(screen, "Axis {} value: {:>6.3f}".format(j, axis))
            command = "Axis {} value: {:>6.3f}\n".format(j, axis)
            usb.write(command.encode())

        textPrint.un_indent()
        buttons = joystick.get_numbuttons()
        textPrint.print(screen, "Number of buttons: {}".format(buttons))
        textPrint.indent()

        for k in range(buttons):
            button = joystick.get_button(k)
            textPrint.print(screen, "Button {:>2} value: {}".format(k, button))
            if button == 1:
                command = "Button {}\n".format(k)
                usb.write(command.encode())

        textPrint.un_indent()
        hats = joystick.get_numhats()
        textPrint.print(screen, "Number of hats: {}".format(hats))
        textPrint.indent()

        for s in range(hats):
            hat = joystick.get_hat(s)
            textPrint.print(screen, "Hat {} value: {}".format(s, str(hat)))

        textPrint.un_indent()
        textPrint.un_indent()
    pygame.display.flip()
    clock.tick(20)
pygame.quit()
