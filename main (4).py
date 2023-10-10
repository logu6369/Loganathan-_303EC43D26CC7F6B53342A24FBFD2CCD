def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices

# Example usage:
products = ["shoes","boot","loafer","shoes","sandal","shoes"]
target="shoes"
target2='apple'
result= linear_search_product(products,target)
print (result )