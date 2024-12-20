import torch

def convert_list_to_tensor(elements):
    # Check for None values
    if any(element is None for element in elements):
        raise ValueError("Error: None values are not allowed in the list.")
    
    # Check for valid element types
    for element in elements:
        if not isinstance(element, (float, str)):
            raise TypeError("Error: Only float and string types are allowed.")
    
    # Convert the list to a tensor
    # Note: PyTorch can handle tensors of homogeneous types, so strings and floats together need special handling.
    # Here, assume a tensor of strings (or floats if that's the case).
    if all(isinstance(element, float) for element in elements):
        # If all elements are floats, create a tensor of floats
        tensor = torch.tensor(elements, dtype=torch.float)
    else:
        # If there are strings, convert all elements to strings first
        elements = [str(e) for e in elements]
        tensor = torch.tensor(elements, dtype=torch.string)
    
    return tensor

# Example usage:
elements = [1.0, 2.5, 3.3]
tensor = convert_list_to_tensor(elements)
print(tensor)