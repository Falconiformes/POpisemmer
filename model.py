# variables
c = 1.0
A1 = 10**-4
A2 = 40*10**-4
h=0.30

# fucnctions

def v_bottom_verandering():
    v1 = c*h
    return v1

def v_h_verandering(v1):
    v2 = -A1/A2*v1
    return v2

while True:
    if h < 0.0001:
        break
    tijd_list = []
    hoogte_list = []
    t = 0
    v_h_verandering(v_bottom_verandering())
    h += v_bottom_verandering()*t
    t += 0.1
    tijd_list += t
    hoogte_list += h

print(tijd_list,hoogte_list)
