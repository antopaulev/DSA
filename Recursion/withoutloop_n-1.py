# Print without loop from N to 1
def func(i , n):
    if i > n:
        return
    func(i + 1, n)
    print(i)

# Example usage
func(1, 5)