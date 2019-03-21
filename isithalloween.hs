main = interact (writeOutput . solve . readInput)

readInput :: String -> [String]
readInput = words

writeOutput :: String -> String
writeOutput = id

solve :: [String] -> String
solve l
    | isHalloween l = "yup"
    | otherwise = "nope"

isHalloween :: [String] -> Bool
isHalloween (m:d:[])
    | m == "OCT" && d == "31" = True
    | m == "DEC" && d == "25" = True
    | otherwise = False
