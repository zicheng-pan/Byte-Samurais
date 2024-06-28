const vehicleDataCol = [
  {
    title: 'engine_condition',
    dataIndex: 'engine_condition',
    key: 'engine_condition'
  },
  {
    title: 'engine_rpm',
    dataIndex: 'engine_rpm',
    key: 'engine_rpm'
  },
  {
    title: 'lub_oil_pressure',
    dataIndex: 'lub_oil_pressure',
    key: 'lub_oil_pressure'
  },
  {
    title: 'fuel_pressure',
    dataIndex: 'fuel_pressure',
    key: 'fuel_pressure'
  },
  {
    title: 'coolant_pressure',
    dataIndex: 'coolant_pressure',
    key: 'coolant_pressure'
  },
  {
    title: 'lub_oil_temp',
    dataIndex: 'lub_oil_temp',
    key: 'lub_oil_temp'
  },
  {
    title: 'coolant_temp',
    dataIndex: 'coolant_temp',
    key: 'coolant_temp'
  },
  {
    title: 'operation',
    dataIndex: 'operation',
    key: 'operation'
  }
];

const vehicleData = [
  {
    key: 'heathyData',
    engine_condition: 'healthy',
    engine_rpm: 473,
    lub_oil_pressure: 3.707835,
    fuel_pressure: 19.510172,
    coolant_pressure: 3.727455,
    lub_oil_temp: 74.129907,
    coolant_temp: 71.774629
  },
  {
    key: 'unheathyData',
    engine_condition: 'unhealthy',
    engine_rpm: 619,
    lub_oil_pressure: 5.672919,
    fuel_pressure: 15.738871,
    coolant_pressure: 2.052251,
    lub_oil_temp: 78.396989,
    coolant_temp: 87.000225
  }
];

export { vehicleDataCol, vehicleData };
