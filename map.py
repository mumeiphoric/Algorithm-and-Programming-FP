'''

MAP LAYOUT

'''
   
layout = [
['1', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '2'],
['|', '1', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '2', '1', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '2', '|'],
['|', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '|'],
['|', '|', ' ', '1', '=', '=', '2', ' ', '1', '=', '=', '=', '2', ' ', '|', '|', ' ', '1', '=', '=', '=', '2', ' ', '1', '=', '=', '2', ' ', '|', '|'],
['|', '|', 'o', '|', '#', '#', '|', ' ', '|', '#', '#', '#', '|', ' ', '|', '|', ' ', '|', '#', '#', '#', '|', ' ', '|', '#', '#', '|', 'o', '|', '|'],
['|', '|', ' ', '3', '=', '=', '4', ' ', '3', '=', '=', '=', '4', ' ', '3', '4', ' ', '3', '=', '=', '=', '4', ' ', '3', '=', '=', '4', ' ', '|', '|'],
['|', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '|'],
['|', '|', ' ', '1', '=', '=', '2', ' ', '1', '2', ' ', '1', '=', '=', '=', '=', '=', '=', '2', ' ', '1', '2', ' ', '1', '=', '=', '2', ' ', '|', '|'],
['|', '|', ' ', '3', '=', '=', '4', ' ', '|', '|', ' ', '3', '=', '=', '2', '1', '=', '=', '4', ' ', '|', '|', ' ', '3', '=', '=', '4', ' ', '|', '|'],
['|', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', '|', ' ', ' ', ' ', ' ', '|', '|', ' ', ' ', ' ', ' ', '|', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', '|'],
['|', '3', '=', '=', '=', '=', '2', ' ', '|', '3', '=', '=', '2', '#', '|', '|', '#', '1', '=', '=', '4', '|', ' ', '1', '=', '=', '=', '=', '4', '|'],
['|', '#', '#', '#', '#', '#', '|', ' ', '|', '1', '=', '=', '4', '#', '3', '4', '#', '3', '=', '=', '2', '|', ' ', '|', '#', '#', '#', '#', '#', '|'],
['|', '#', '#', '#', '#', '#', '|', ' ', '|', '|', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '|', '|', ' ', '|', '#', '#', '#', '#', '#', '|'],
['4', '#', '#', '#', '#', '#', '|', ' ', '|', '|', '#', '1', '=', '=', '-', '-', '=', '=', '2', '#', '|', '|', ' ', '|', '#', '#', '#', '#', '#', '3'],
['=', '=', '=', '=', '=', '=', '4', ' ', '3', '4', '#', '|', '#', '#', '#', '#', '#', '#', '|', '#', '3', '4', ' ', '3', '=', '=', '=', '=', '=', '='],
['#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '|', '#', '#', '#', '#', '#', '#', '|', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#'],
['=', '=', '=', '=', '=', '=', '2', ' ', '1', '2', '#', '|', '#', '#', '#', '#', '#', '#', '|', '#', '1', '2', ' ', '1', '=', '=', '=', '=', '=', '='],
['2', '#', '#', '#', '#', '#', '|', ' ', '|', '|', '#', '3', '=', '=', '=', '=', '=', '=', '4', '#', '|', '|', ' ', '|', '#', '#', '#', '#', '#', '1'],
['|', '#', '#', '#', '#', '#', '|', ' ', '|', '|', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '|', '|', ' ', '|', '#', '#', '#', '#', '#', '|'],
['|', '#', '#', '#', '#', '#', '|', ' ', '|', '|', '#', '1', '=', '=', '=', '=', '=', '=', '2', '#', '|', '|', ' ', '|', '#', '#', '#', '#', '#', '|'],
['|', '1', '=', '=', '=', '=', '4', ' ', '3', '4', '#', '3', '=', '=', '2', '1', '=', '=', '4', '#', '3', '4', ' ', '3', '=', '=', '=', '=', '2', '|'],
['|', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '|'],
['|', '|', ' ', '1', '=', '=', '2', ' ', '1', '=', '=', '=', '2', ' ', '|', '|', ' ', '1', '=', '=', '=', '2', ' ', '1', '=', '=', '2', ' ', '|', '|'],
['|', '|', ' ', '3', '=', '2', '|', ' ', '3', '=', '=', '=', '4', ' ', '3', '4', ' ', '3', '=', '=', '=', '4', ' ', '|', '1', '=', '4', ' ', '|', '|'],
['|', '|', 'o', ' ', ' ', '|', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '|', ' ', ' ', 'o', '|', '|'],
['|', '3', '=', '2', ' ', '|', '|', ' ', '1', '2', ' ', '1', '=', '=', '=', '=', '=', '=', '2', ' ', '1', '2', ' ', '|', '|', ' ', '1', '=', '4', '|'],
['|', '1', '=', '4', ' ', '3', '4', ' ', '|', '|', ' ', '3', '=', '=', '2', '1', '=', '=', '4', ' ', '|', '|', ' ', '3', '4', ' ', '3', '=', '2', '|'],
['|', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', '|', ' ', ' ', ' ', ' ', '|', '|', ' ', ' ', ' ', ' ', '|', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', '|'],
['|', '|', ' ', '1', '=', '=', '=', '=', '4', '3', '=', '=', '2', ' ', '|', '|', ' ', '1', '=', '=', '4', '3', '=', '=', '=', '=', '2', ' ', '|', '|'],
['|', '|', ' ', '3', '=', '=', '=', '=', '=', '=', '=', '=', '4', ' ', '3', '4', ' ', '3', '=', '=', '=', '=', '=', '=', '=', '=', '4', ' ', '|', '|'],
['|', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '|'],
['|', '3', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '4', '|'],
['3', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '4']
         ]

'''

' ' ==> Traversable path with little pellets
'o' ==> Traversable path with power-up pellets

'-' ==> Gate for ghosts

'=' ==> Horizontal border
'|' ==> Vertical border
'1' ==> Top left corner border
'2' ==> Top right corner border
'3' ==> Bottom left corner border
'4' ==> Bottom right corner border

'#' ==> Hollow

'''