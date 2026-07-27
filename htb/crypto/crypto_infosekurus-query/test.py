import math
from Crypto.Util.number import long_to_bytes as l2b

N   = 96124936107896748280555244677021991330091778649135119790286533059582754409293601619525608937362904170585046388534482094091790568122866360316740693418876264680551778543440000535075643338759767637391693271627644627735703513501276657327234250653312367333508135208249266632071094632385510113463482633032902002209
phi = 96124936107896748280555244677021991330091778649135119790286533059582754409293601619525608937362904170585046388534482094091790568122866360316740693418876244909857319694820595566002064612532239556729264541411304166794719906273078548635013448269328260390344716890710955831745947175474039259985922959198890019520
e   = 8192
ct  = 51816728896765729165186021366650033922161854260023765926516764212380080999428031782403692554840944650728149224007813256112542753403798488931333180010037031802978995236260881180744509643568609667946059177080900002207286170959293367981118480670733346922872171728818445828772712223189919802938914693896148309743

s = N - phi + 1
disc = s*s - 4*N
root = math.isqrt(disc)
assert root*root == disc
p = (s + root)//2
q = (s - root)//2
assert p*q == N

def v2(n):
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k, n

def tonelli(n, p):
    if n % p == 0:
        return 0
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1)//4, p)
    z = 2
    while pow(z, (p-1)//2, p) != p - 1:
        z += 1
    c = pow(z, q, p)
    r = pow(n, (q+1)//2, p)
    t = pow(n, q, p)
    m = s
    while t != 1:
        i, t2 = 0, t
        while t2 != 1:
            t2 = pow(t2, 2, p)
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r

def extgcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extgcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def all_eth_roots(c, e, p):
    k2, m = v2(p - 1)
    ke, eo = v2(e)
    kmin = min(k2, ke)
    two_k2 = 1 << k2

    g_, a, b = extgcd(m, two_k2)
    assert g_ == 1
    c_2part = pow(c, (a * m) % (p - 1), p)
    c_mpart = pow(c, (b * two_k2) % (p - 1), p)

    assert math.gcd(eo, m) == 1
    e_inv_mod_m = pow(e % m, -1, m)
    x_mpart = pow(c_mpart, e_inv_mod_m, p)

    eo_inv_mod_2k2 = pow(eo % two_k2, -1, two_k2) if two_k2 > 1 else 0
    target = pow(c_2part, eo_inv_mod_2k2, p) if two_k2 > 1 else c_2part

    roots_2part = [target]
    for _ in range(kmin):
        new_roots = []
        for r in roots_2part:
            rt = pow(r, (p + 1)//4, p) if p % 4 == 3 else tonelli(r, p)
            if pow(rt, 2, p) == r % p:
                new_roots.append(rt)
                new_roots.append((p - rt) % p)
        roots_2part = new_roots

    return sorted(set((r2 * x_mpart) % p for r2 in roots_2part))

roots_p = all_eth_roots(ct % p, e, p)
roots_q = all_eth_roots(ct % q, e, q)
print("roots mod p:", len(roots_p), "roots mod q:", len(roots_q))

def crt(a, m1, b, m2):
    m1_inv = pow(m1, -1, m2)
    return (a + m1 * ((b - a) * m1_inv % m2)) % (m1 * m2)

candidates = [crt(rp, p, rq, q) for rp in roots_p for rq in roots_q]
print("total candidates:", len(candidates))

valid = [x for x in candidates if pow(x, e, N) == ct]
print(len(valid), "of", len(candidates), "verify correctly against ct")

print("\n--- valid candidate bytes ---")
for x in valid:
    try:
        b = l2b(x)
        print(repr(b))
    except Exception as ex:
        print("err converting:", ex)