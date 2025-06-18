from typing import List, Dict, Any
from .parameters_rooms_and_structures import Rooms


class MergeSort:
    STRUCTURES = {}
    ENEMIES = {}

    @staticmethod
    def _sort(arr: List[int]) -> List[int]:
        half_len_array: int = len(arr)//2
        first_half_array: List[int] = arr[:half_len_array]
        second_half_array: List[int] = arr[half_len_array:]

        if len(first_half_array) > 1:
            first_half_array = MergeSort._sort(first_half_array)
        if len(second_half_array) > 1:
            second_half_array = MergeSort._sort(second_half_array)

        return MergeSort._merge(first_half_array, second_half_array)

    @staticmethod
    def _merge(first_half: List[int], second_half: List[int]) -> List[int]:
        sorted_list: List[int] = []
        len_first_half_array: int = len(first_half)
        len_second_half_array: int = len(second_half)
        i_first_array: int = 0
        i_second_array: int = 0

        while i_first_array < len_first_half_array and i_second_array < len_second_half_array:
            if first_half[i_first_array] <= second_half[i_second_array]:
                sorted_list.append(first_half[i_first_array])
                i_first_array += 1
            else:
                sorted_list.append(second_half[i_second_array])
                i_second_array += 1

        sorted_list += first_half[i_first_array:] + second_half[i_second_array:]
        return sorted_list

    @staticmethod
    def _sort_rooms(rooms: Dict[int, Dict[str, Any]]) -> Dict[int, Dict[str, Any]]:
        sorted_keys = MergeSort._sort(list(rooms.keys()))
        sorted_rooms: Dict[int, Dict[str, Any]] = {}
        for key in sorted_keys:
            sorted_rooms[key] = rooms[key]
        return sorted_rooms

    @staticmethod
    def get_sorted_list_structures(rooms: Dict[int, Dict[str, Any]], number_level: int):
        if number_level in MergeSort.STRUCTURES.keys():
            return MergeSort.STRUCTURES[number_level]
        sorted_list = MergeSort._sort_rooms(rooms)
        MergeSort.STRUCTURES[number_level] = sorted_list
        return sorted_list

    @staticmethod
    def get_sorted_list_enemies(rooms: Dict[int, Dict[str, Any]], number_level: int):
        if number_level in MergeSort.ENEMIES.keys():
            return MergeSort.ENEMIES[number_level]
        sorted_list = MergeSort._sort_rooms(rooms)
        MergeSort.ENEMIES[number_level] = sorted_list
        return sorted_list


class BinarySearch:

    @staticmethod
    def find(rooms: Dict[int, Dict[str, Any]], target: int, key: str = None):
        if key == "structures":
            array = MergeSort.get_sorted_list_structures(rooms, Rooms.NUMBER_LEVEL)
        else:
            array = MergeSort.get_sorted_list_enemies(rooms, Rooms.NUMBER_LEVEL)
        keys_array = list(array.keys())
        values_array = list(array.values())
        min_index: int = 0
        max_index: int = len(keys_array) - 1

        while max_index >= min_index:
            mid_index = (max_index + min_index) // 2
            if keys_array[mid_index] == target:
                return values_array[mid_index]
            elif keys_array[mid_index] < target:
                min_index = mid_index + 1
            else:
                max_index = mid_index - 1


def get_objects(rooms: Dict[int, Dict[str, Any]], target: int, key: str = None):
    return BinarySearch.find(rooms, target, key)

