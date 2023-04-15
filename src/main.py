from latex_var import latex_var
from sage.all import *

q_L, q_R, q_O, q_M, q_C = latex_var("\mathbf{q_L} \mathbf{q_R} \mathbf{q_O} \mathbf{q_M} \mathbf{q_C}")
a, b, c, u, e, r = latex_var("\mathbf{a} \mathbf{b} \mathbf{c} u \mathbf{e} r")
a1, b1, c1, u1, e1, r1 = latex_var("\mathbf{a}'_n \mathbf{b}'_n \mathbf{c}'_n u'_n \mathbf{e}'_n r'_n")
a2, b2, c2, u2, e2, r2 = latex_var("\mathbf{a}_n \mathbf{b}_n \mathbf{c}_n u_n \mathbf{e}_n r_n")


# Define plonk constraint as lambda
# C(a, b, c, u, e) = u (q_L a + q_R b + q_O c) q_M a b + q_C u^2 + e

C = lambda a, b, c, u, e: u * (q_L * a + q_R * b + q_O * c) + q_M * a * b + q_C * u**2 + e
T = lambda a1, b1, c1, u1, a2, b2, c2, u2: \
    u2*(q_L*a1 + q_R*b1 + q_O*c1) + u1*(q_L*a2 + q_R*b2 + q_O*c2)+\
    q_M*(a1*b2+a2*b1) + 2*u1*u2*q_C

print("Relaxed PLONK constraint: $${}$$".format(latex(C(a, b, c, u, e))))


t = T(a1, b1, c1, u1, a2, b2, c2, u2)
print("t: ", latex(t))

r = latex_var("r")

u = u1 + r * u2
a = a1 + r * a2
b = b1 + r * b2
c = c1 + r * c2
e = e1 - r * t + r**2 * e2

err = C(a, b, c, u, e) - (C(a1, b1, c1, u1, e1) + r**2 * C(a2, b2, c2, u2, e2))

print("Simplify: ", err.simplify_full())


# try to unroll with another initial row

# assume constratints are executed successfully:
e = -C(a, b, c, u, 0)

a3, b3, c3, u3 = latex_var("\mathbf{a}_{3} \mathbf{b}_{3} \mathbf{c}_{3} u_{3}")

# compute error
e3 = - C(a3, b3, c3, u3, 0)

# compute hiding layer candidate values

u4 = (u - u3)/r
a4 = (a - a3)/r
b4 = (b - b3)/r
c4 = (c - c3)/r

_t = T(a3, b3, c3, u3, a4, b4, c4, u4)

e4 = (e - e3 + r * _t)/r**2

print("err3: ", latex(C(a3, b3, c3, u3, e3).simplify_full()))
print("err4: ", latex(C(a4, b4, c4, u4, e4).simplify_full()))

