import pygame
import time
import math

# Variables/constens
# W and H of the screen
width = 640
hight = 480

# radius and center of the clock
radius = 200
center = (width/2, hight/2)

# Length of clock arms 
s_arm_length = 150 
m_arm_length = 140
h_arm_length = 100

# Draw the screen and color it white 
pygame.init()
screen = pygame.display.set_mode((width,hight))
screen.fill((255,255,255))

# Draw the clock cirkel and the black border around it
pygame.draw.circle((screen),(0,0,0),center,(210))
pygame.draw.circle((screen),(255,255,255),center,(200))

# Draw the pins for the clock
# 60 minuts pins + 12 hour pins = 72 pins
for i in range(72):  # Combined loop for both minuts and hour pins
    if i < 60:
        angle = math.radians(i * (360/60))  # Convert to radians and adjust for 60 positions
        length = 10   #Length of minuts pins
        thickness = 2 #Length of minuts pins
    else:
        angle = math.radians((i - 60) * (360/12))  # Convert to radians and adjust for 12 positions
        length = 20   #Length of the hour pins
        thickness = 4 #Thickness of the hour pins

    # Finding the coordinates of the edge of the clock face
    x1 = center[0] + radius * math.cos(angle)
    y1 = center[1] + radius * math.sin(angle)

    # Finding the coordinates minus the specified length
    x2 = center[0] + (radius - length) * math.cos(angle)
    y2 = center[1] + (radius - length) * math.sin(angle)

    # Drawing the line between the two coordinates
    pygame.draw.line(screen, (0,0,0), (x1, y1), (x2, y2), thickness)



# Game loop
run_falg = True
while run_falg is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_falg = False

# Variables for local time
    lokal_tid = time.localtime()
    
# Draw the update cirkel
    pygame.draw.circle(screen,(255,255,255),center,(s_arm_length + 2))

# Draw the second arm 
    # Angle for the arm
    angle_s = math.radians((lokal_tid.tm_sec) * 6 - 90)

    # End cords for the arm  
    x_s = center[0] + s_arm_length * math.cos(angle_s)
    y_s = center[1] + s_arm_length * math.sin(angle_s)

    # Drawing the line between the 2 cords found 
    pygame.draw.line(screen, (255, 0, 0), center, (x_s, y_s),2)

# Draw the minuts arm 
    # Angle for the arm
    angle_m = math.radians(((lokal_tid.tm_min) + (lokal_tid.tm_sec / 60)) * 6 - 90)

    # End cords for the arm  
    x_m = center[0] + m_arm_length * math.cos(angle_m)
    y_m = center[1] + m_arm_length * math.sin(angle_m)

    # Drawing the line between the 2 cords found 
    pygame.draw.line(screen, (0,0,0), center, (x_m, y_m), 4)

# Draw the hour arm 
    # Angle for the arm
    angle_h = math.radians((((lokal_tid.tm_hour % 12) +
                          ((lokal_tid.tm_min / 60))) * 30 - 90) )

    # End cords for the arm  
    x_h = center[0] + h_arm_length * math.cos(angle_h)
    y_h = center[1] + h_arm_length * math.sin(angle_h)

    # Drawing the line between the 2 cords found 
    pygame.draw.line(screen, (0,0,0), center, (x_h, y_h), 4)

  
#Update the display
    pygame.display.flip() 