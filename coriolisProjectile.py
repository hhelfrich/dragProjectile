import math

g = 9.8 #m/s^2
w = .0000727*math.pi/180 #degrees/s

def acceleration(v_x, v_y, C, m, w, v_z, l):
    a_x = -C*v_x*math.sqrt(v_x*v_x + v_y*v_y + v_z*v_z)/m - 2*v_z*w*math.sin(l)
    a_y = -g - C*v_y*math.sqrt(v_x*v_x + v_y*v_y + v_z*v_z)/m - 2*v_z*w*math.cos(l)
    a_z = -C*v_z*math.sqrt(v_x*v_x + v_y*v_y + v_z*v_z)/m + 2*v_x*w*math.sin(l) + 2*v_y*w*math.cos(l)
    return a_x, a_y, a_z

def update(x, y, z, v_x, v_y, v_z, a_x, a_y, a_z, dt):
    x = x + v_x*dt + 0.5*a_x*dt*dt
    y = y + v_y*dt + 0.5*a_y*dt*dt
    z = z + v_z*dt + 0.5*a_z*dt*dt
    v_x = v_x + a_x*dt
    v_y = v_y + a_y*dt
    v_z = v_z + a_z*dt
    return x, y, z, v_x, v_y, v_z

v_0 = float(input("What is the magnitude of the initial velocity?: "))
theta = float(input("What is the launch angle in degrees?: "))
dt = float(input("What is the size of the timestep?: "))
m = float(input("What is the projectile mass?: "))
C = float(input("What is the drag coefficient?: "))
l = float(input("What is the latitude?: "))

v_x = v_0*math.cos(theta*math.pi/180.0)
v_y = v_0*math.sin(theta*math.pi/180.0)
v_z = 0

outFile = open("coriolisProjectile.txt", "w")

t = 0
x = 0
y = 0
z = 0
y_max = 0
inFlight = True

while (inFlight):
    a_x, a_y, a_z = acceleration(v_x, v_y, C, w, m, v_z, l)
    x, y, z, v_x, v_y, v_z = update(x, y, z, v_x, v_y, v_z, a_x, a_y, a_z, dt)
    t += dt
    if (y >= 0):
        outFile.write(str(t) + " " + str(x) + " " + str(y) + " " + str(z) + " " + str(v_x) + " " + str(v_y) + " " + str(v_z) + " " + str(a_x) + " " + str(a_y) + " "  + str(a_z) + " " + "\n")
        if (y > y_max):
            y_max = y 
    else:
        inFlight = False

outFile.close()

print("The maximum height was", y_max)
print("the horizontal range was", x)
