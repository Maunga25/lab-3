from tabulate import tabulate

object_names = ['в','п','б','а','и','н','т','о','ф','к','р']
objects_space = [3,2,2,2,1,1,3,1,1,2,2]
objects_Points = [25,15,15,20,5,15,20,25,15,20,20]
objects_dict = dict(zip(object_names, objects_space))
total_space = 8
Survival_Points = 25


def optimize(object_names=object_names, objects_space=objects_space, objects_Points=objects_Points,totalSpace=total_space,
            Survival_Points=Survival_Points):
   Table = []
   Combination = []
   numberOfObjects = len(objects_space)

   for object_index in range(numberOfObjects + 1):
       Table.append([0] * (totalSpace + 1))
       Combination.append([[]] * (totalSpace + 1))

   for object_index in range(numberOfObjects + 1):
       for space in range(totalSpace + 1):
           if object_index == 0 or space == 0:
               Table[object_index][space] = Survival_Points
               Combination[object_index][space] = []
           else:
               if objects_space[object_index - 1] <= space:
                   Table[object_index][space] = max(
                       objects_Points[object_index - 1] + Table[object_index - 1][space - objects_space[object_index - 1]],
                       Table[object_index - 1][space])
                   if max(objects_Points[object_index - 1] + Table[object_index - 1][space - objects_space[object_index - 1]],
                          Table[object_index - 1][space]) == objects_Points[object_index - 1] + Table[object_index - 1][
                       space - objects_space[object_index - 1]]:
                       Combination[object_index][space] = Combination[object_index - 1][
                                                               space - objects_space[object_index - 1]] + [
                                                               object_names[object_index - 1]]
                   else:
                       Combination[object_index][space] = Combination[object_index - 1][space]

               else:
                   Table[object_index][space] = Table[object_index - 1][space]
                   Combination[object_index][space] = Combination[object_index - 1][space]

   return Table, Combination, Table[numberOfObjects][totalSpace],  Combination[numberOfObjects][totalSpace]


maxPoint = optimize()[2]
maxCombo = optimize()[3]
finalPoint = maxPoint-(sum(objects_Points)-maxPoint)

def createArray(gridColumn, maxPoint = maxPoint, maxCombo = maxCombo, objects_dict = objects_dict, finalPoint= finalPoint):
   if finalPoint >= 0:
       solutionList = ['[д] ']
       for key in maxCombo:
           for i in range(objects_dict[key]):
               solutionList.append(f'[{key}] ')
       solution = ''
       for a in solutionList:
           if (len(solution.replace('\n', '')) / 4) % gridColumn == 0:
               solution += '\n'
           solution += a
       solution += f'\n очки выживания: {finalPoint}'
       return solution
   else:
       return'нет решения'
print(f'1. варианта 6 {createArray(3)}')
#1.Допзадание
optimized = optimize(totalSpace=6)
maxPoint = optimized[2]
maxCombo = optimized[3]
dopFinal = maxPoint-(sum(objects_Points)-maxPoint)
print(f'\n1.7 ячеек.{createArray(3, maxPoint=maxPoint, maxCombo=maxCombo, finalPoint=dopFinal)}')

#2.Допзадание возможные комбинации с положительными результатами
Table = optimize()[0]
Combination = optimize()[1]
print('комбинации вещей у которых общий счёт положительный')

for i in range(len(objects_space)+1):
   for j in range(total_space):
       if (Table[i][j]-(sum(objects_Points)-Table[i][j])) > 0:
           print(Combination[i][j])


