/**
 * @param dateString string assumed to be in format 2000-01-02
 * @returns string reformatted to 02/01/2000
 */
function formatDate(dateString: string) {
  return `${dateString.substring(8, 10)}/${dateString.substring(5, 7)}/${dateString.substring(
    0,
    4
  )}`
}
export default formatDate
