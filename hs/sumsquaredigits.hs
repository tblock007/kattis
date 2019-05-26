main = interact (writeOutput . solve . readInput)

readInput :: String -> [(Int, Int, Int)]
readInput s = (map toTriple) $ tail $ lines s
    where 
        toTriple :: String -> (Int, Int, Int)
        toTriple s = let (a:b:c:[]) = words s in (read a, read b, read c)

writeOutput :: [(Int, Int)] -> String
writeOutput = unlines . (map toLine)
    where 
        toLine :: (Int, Int) -> String
        toLine (a, b) = show a ++ " " ++ show b

solve :: [(Int, Int, Int)] -> [(Int, Int)]
solve = map solveInstance

solveInstance :: (Int, Int, Int) -> (Int, Int)
solveInstance (k, b, x) = (k, ssd b x)
    where 
        ssd :: Int -> Int -> Int
        ssd b 0 = 0
        ssd b x = (mod x b) * (mod x b) + (ssd b (quot x b))
