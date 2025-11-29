function countWorkingDays(year) {
  const holidays = [
    `${year}-01-07`,
    `${year}-04-13`,
    `${year}-04-14`,
    `${year}-04-15`,
    `${year}-11-09`
  ]

  function isHoliday(dateStr) {
    return holidays.includes(dateStr)
  }

  let totalWorkingDays = 0

  let current = new Date(year, 0, 1)
  const end = new Date(year, 11, 31)
  while (current <= end) {
    const day = current.getDay()
    const dateStr = current.toISOString().split("T")[0]

    if (day === 0) {
    } else if (day === 6) {
      totalWorkingDays += 0.5
    } else if (isHoliday(dateStr)) {
    } else {
      totalWorkingDays += 1
    }

    current.setDate(current.getDate() + 1)
  }

  return totalWorkingDays
}

console.log(countWorkingDays(2024))
