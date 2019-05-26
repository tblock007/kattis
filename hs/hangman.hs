main = interact (writeOutput . solve . readInput)

readInput :: String -> [String]
readInput = lines

writeOutput :: String -> String
writeOutput = id

solve :: [String] -> String
solve (w:o:[]) = solveAux w o 0

solveAux :: String -> String -> Int -> String
solveAux w o c 
    | c == 10 = "LOSE"
    | length w == 0 = "WIN"
    | correct w (head o) = solveAux [cc | cc <- w, cc /= (head o)] (tail o) c
    | otherwise = solveAux w (tail o) (c + 1)
    
correct :: String -> Char -> Bool
correct w c = elem c w
