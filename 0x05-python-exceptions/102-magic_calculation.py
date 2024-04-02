#!/usr/bin/python3

def magic_calculation(a, b):
    glb = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Excetion("Toofar")
            else:
                glb += a ** b
        except Exception:
            glb = a+b
            break
        return glb
