E = set(map(int, input("Enter elements of set E separated by spaces: ").split()))
N = set(map(int, input("Enter elements of set N separated by spaces: ").split()))
print("Union of E and N is", E | N)
print("Intersection of E and N is", E & N)
print("Difference of E and N is", E - N)
print("Symmetric difference of E and N is", E ^ N)
