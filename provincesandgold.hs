main = interact (writeOutput . solve . readInput)

readInput :: String -> [Int]
readInput = (map read) . words

writeOutput :: String -> String
writeOutput = (++"\n")

solve :: [Int] -> String
solve coins = formstring (bestv power) (bestt power)
    where 
        power = bp coins

bp :: [Int] -> Int
bp (g:s:c:[]) = 3 * g + 2 * s + c

bestv :: Int -> Maybe String
bestv b 
    | b >= 8 = Just "Province"
    | b >= 5 = Just "Duchy"
    | b >= 2 = Just "Estate"
    | otherwise = Nothing

bestt :: Int -> String
bestt b
    | b >= 6 = "Gold"
    | b >= 3 = "Silver"
    | otherwise = "Copper"

formstring :: Maybe String -> String -> String
formstring (Nothing) t = t
formstring (Just v) t = v ++ " or " ++ t