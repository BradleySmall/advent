def get_input():
    with open("input.txt") as f:
        data = f.readline()
    return data


def main():
    data = get_input()

    layer_size = 150
    image = []
    for i in range(layer_size, len(data) + 1, layer_size):
        b = i - layer_size
        image.append(data[b:i])

    image_dict = {e : list(i) for e, i in enumerate(image) }
    
    layer_list = [layer for layer in image_dict.values()]
        
    print(layer_list[:2])    

    # print(image_dict)
    # for layer in image_dict:
    #     new_dict = {}
    #     for i in list(image_dict[layer]):
    #         new_dict[i] = new_dict.get(i, 0) + 1
    #     image_dict[layer] = new_dict

    # big = 99999
    # idx = -1
    # for i in image_dict:
    #     if image_dict[i]['0'] < big:
    #         big = image_dict[i]['0']
    #         idx = i

    # print(idx, image_dict[idx]['0'],image_dict[idx]['1'],image_dict[idx]['2'], image_dict[idx]['1']*image_dict[idx]['2'])

if __name__=='__main__':
    main()

