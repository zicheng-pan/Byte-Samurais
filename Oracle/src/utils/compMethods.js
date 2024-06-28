import { other } from '@/constant/vehicleModel';

const getTargetOptionLabel = (options = [], target, mode) => {
  const resOpt = options.find(item => (item.value || '').toString() === (target || '').toString());
  let res = mode === 'edit' ? resOpt?.value : resOpt?.label;
  return res;
};

const parseVehicleModelSelectOptions = param => {
  let options = param.data || [];
  let selectDataByType = {};
  options.forEach(item => {
    item.label = item.itemCname;
    item.value = item.itemCode;
    if (selectDataByType[item.itemType]) {
      selectDataByType[item.itemType].push(item);
    } else {
      selectDataByType[item.itemType] = [item];
    }
  });
  return selectDataByType;
};

const addOtherOption = param => {
  if (!Array.isArray(param)) return [];
  let res = [...param];
  if (param.filter(item => item.itemEname.toLowerCase().includes('other')).length === 0) {
    res = [...param, ...other];
  }
  return res;
};

const checkOtherOption = (setMethod, targetVal, options, setCustomVal) => {
  const fullOptions = addOtherOption(options);
  const targetItem = fullOptions.filter(item => item.value === targetVal)[0];
  const check =
    (targetItem?.itemEname || targetItem?.value || '').toLowerCase().includes('other') ||
    (targetItem?.itemCname || '').includes('其他');
  if (check) {
    typeof setCustomVal === 'function' && setCustomVal('');
    return setMethod(true);
  } else {
    typeof setCustomVal === 'function' && setCustomVal(targetItem?.itemCname);
  }
  return setMethod(check);
};

const setSelectLabel = (targetVal, options, setValFunc) => {
  const opt = Array.isArray(options) ? options : [];
  const targetItem = opt.filter(item => item.value === targetVal)[0];
  setValFunc(targetItem?.itemCname);
};

export {
  getTargetOptionLabel,
  parseVehicleModelSelectOptions,
  addOtherOption,
  checkOtherOption,
  setSelectLabel
};
