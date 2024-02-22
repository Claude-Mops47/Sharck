function longestConsecutiveOnes(binaryNumber) {
  const binaryString = binaryNumber.toString(2);
  let maxLength = 0;
  let currentLength = 0;

  for (let i = 0; i < binaryString.length; i++) {
    if (binaryString[i] === "1") {
      currentLength++;
      maxLength = Math.max(maxLength, currentLength);
    } else {
      currentLength = 0;
    }
  }
  return maxLength;
}

const number = 10111011011101;
const longestOnes = longestConsecutiveOnes(number);

console.log(longestOnes);
