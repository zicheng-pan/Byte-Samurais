const checkNullorUndefined = param => {
  return param === null || param === undefined;
};

const sumUp = (...param) => {
  let res = 0;
  param.forEach(item => (res += item));
  return res;
};

export { sumUp, checkNullorUndefined };
