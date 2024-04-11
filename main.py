from typing import List

def find_indices(nums: List[int], target: int) -> List[int]:
    num_index_map = {}
    for index, num in enumerate(nums):
        complement_index = num_index_map.get(target - num)
        if complement_index is not None and complement_index != index:
            return [complement_index, index]  # 순서가 바뀌도록 수정
        num_index_map[num] = index
    return []