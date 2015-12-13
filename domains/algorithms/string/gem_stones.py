


def number_of_gem_elements(rocks):
  unique_rocks = [{element: True for element in rock} for rock in rocks]
  rock_counts = {element: 0 for rock in rocks for element in rock}
  for rock in unique_rocks:
    for element, count in rock_counts.items():
      if rock.get(element, False):
        rock_counts[element] += 1

  return sum([1 for element, count in rock_counts.items() if count == len(rocks)])



if __name__ == '__main__':
  number_of_cases = int(raw_input())
  print number_of_gem_elements([raw_input() for _ in range(number_of_cases)])