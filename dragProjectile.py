import math

g = 9.8 #m/s^2

def acceleration(v_x, v_y, C, m):
    a_x = -C*v_x*math.sqrt(v_x*v_x + v_y*v_y)/m
    a_y = -g - C*v_y*math.sqrt(v_x*v_x + v_y*v_y)/m
    return a_x, a_y

def update(x, y, v_x, v_y, a_x, a_y, dt):
    x = x + v_x*dt + 0.5*a_x*dt*dt
    y = y + v_y*dt + 0.5*a_y*dt*dt
    v_x = v_x + a_x*dt
    v_y = v_y + a_y*dt
    return x, y, v_x, v_y

v_0 = float(input("What is the magnitude of the initial velocity?: "))
theta = float(input("What is the launch angle in degrees?: "))
dt = float(input("What is the size of the timestep?: "))
m = float(input("What is the projectile mass?: "))
C = float(input("What is the drag coefficient?: "))

v_x = v_0*math.cos(theta*math.pi/180.0)
v_y = v_0*math.sin(theta*math.pi/180.0)

outFile = open("dragProjectile.txt", "w")

t = 0
x = 0
y = 0
z = 0
y_max = 0
inFlight = True

while (inFlight):
    a_x, a_y = acceleration(v_x, v_y, C, m)
    x, y, v_x, v_y = update(x, y, v_x, v_y, a_x, a_y, dt)
    t += dt
    if (y >= 0):
        outFile.write(str(t) + " " + str(x) + " " + str(y) + " " + str(z) + " " + str(v_x) + " " + str(v_y) + " " + str(a_x) + " " + str(a_y) + " " + "\n")
        if (y > y_max):
            y_max = y 
    else:
        inFlight = False

outFile.close()

print("The maximum height was", y_max)
print("the horizontal range was", x)
