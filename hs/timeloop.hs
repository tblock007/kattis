main = interact (writeOutput . solve . readInput)

readInput :: String -> Int
readInput = read

writeOutput :: [String] -> String
writeOutput = unlines

solve :: Int -> [String]
solve n = genLine n 1

genLine :: Int -> Int -> [String]
genLine n c 
    | n == c = [(show c ++ " Abracadabra")]
    | otherwise = (show c ++ " Abracadabra") : genLine n (c + 1)
