def linear_search_product(products, target_product):
    """
    Performs a linear search to find the target product in the list.
    
    Args:
        products (list): List of product names.
        target_product (str): The product name to search for.
    
    Returns:
        list: A list of indices of all occurrences of the target product, or an empty list if not found.
    """
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices

# Example usage:
products_list = ["apple", "banana", "apple", "orange", "apple"]
target = "apple"
result = linear_search_product(products_list, target)
print(f"Indices of '{target}': {result}")
