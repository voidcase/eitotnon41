from hashlib import sha256
import random

K_SIZE = 16

def h(v:str, k:str, x_size: int) -> str:
    vk_bytes = bytes.fromhex((v + k).zfill(6))
    hash_digest = bin(int.from_bytes(sha256(vk_bytes).digest(), byteorder='big'))
    return hash_digest[2:2+x_size]

def gen_k() -> int:
    return random.getrandbits(K_SIZE)

def has_k(v:int, x:str) -> bool:
    x_size = len(x)
    for cheat_k in range(2**K_SIZE):
        cheat_x = h(str(v), str(cheat_k), x_size)
        if cheat_x == x:
            return True
    return False

def try_to_unbind(x_size:int) -> bool:
    k = gen_k()
    v = random.randint(0,1)
    x = h(str(v), str(k), x_size)
    return has_k(int(not v), x)

def find_prob(func, x_size:int, iterations:int=100) -> float:
    success = 0
    for i in range(iterations):
        if func(x_size):
            success += 1
    return success / iterations 

def try_to_unveil(x_size:int) -> bool:
    k = gen_k()
    v = random.randint(0,1)
    x = h(str(v), str(k), x_size)
    return has_k(0, x) ^ has_k(1, x)


if __name__ == '__main__':
    [print('x_size:', i, '\tprob:', find_prob(try_to_unveil, i)) for i in range(256)]
    
