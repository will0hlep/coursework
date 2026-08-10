//lesson 1
export function averageScore(ratings: number[]) {
  const count = ratings.length
  if (count === 0) {
    return 0;
  }
  let total = 0;
  for (const rating of ratings) {
    total += rating;
  }
  return total / count;
}

//lesson 3
export function interpolateComment(
  id: number,
  comment: string,
  comments: (string | number)[],
) {
  const index = comments.findIndex((c) => c === id);
  if (index !== -1) {
    comments[index] = comment;
  }
}

//lesson 4
export function formatLabels(...labels: string[]) {
  const count = labels.length
  if (count === 0) {
    return "No Labels";
  } 
  return `Label${count === 1? "": "s"}: ${labels.join(", ")}`;
}

//lesson 5
export function collectSupportData(id: number, resolved: boolean) {
  const supportData = [];
  supportData.push("Support session started");
  supportData.push(id);
  supportData.push(resolved);
  return supportData;
}
