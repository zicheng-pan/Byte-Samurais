import React, { useState, useEffect } from 'react';
import { Button, Modal, Skeleton, Table } from 'antd';
import AI from '@/asset/image/AI.svg';
import car from '@/asset/image/rangeRover.png';
import store from '@/asset/image/4S.jpg';
import iphone from '@/asset/image/iphone.svg';
import { ArrowRightOutlined, ArrowUpOutlined, SwapOutlined } from '@ant-design/icons';
import { vehicleDataCol, vehicleData } from '@/constant/VCPS.js';
import styles from './index.module.less';

const PredictionSystem = () => {
  const [isVcdpModalOpen, setIsVcdpModalOpen] = useState(false);
  const [isClientModalOpen, setIsClientModalOpen] = useState(false);
  const [isVehicleModalOpen, setIsVehicleModalOpen] = useState(false);
  const [vehicleUploadData, setVehicleUploadData] = useState(null);
  const [alarmInfo, setAlarmInfo] = useState(null);

  const vehicleDColforShown = vehicleDataCol.filter(item => item.dataIndex !== 'operation');

  useEffect(() => {
    let target = vehicleDataCol.find(item => item.dataIndex === 'operation');
    target.render = (_, record) => {
      return (
        <div>
          <Button className={styles.sendBtn} onClick={() => sendData(record)} type={'primary'}>
            send
          </Button>
        </div>
      );
    };
  }, []);

  useEffect(() => {
    if (vehicleUploadData?.engine_condition === 'unhealthy') {
      setTimeout(() => {
        setAlarmInfo(vehicleUploadData);
      }, 2000);
    }
  }, [vehicleUploadData]);

  const sendData = record => {
    setVehicleUploadData(record);
  };

  const openVcdpModel = () => {
    if (!isVcdpModalOpen) {
      setIsVcdpModalOpen(true);
    }
  };

  const openClientModel = () => {
    if (!isClientModalOpen) {
      setIsClientModalOpen(true);
    }
  };

  const openVehicleModel = () => {
    if (!isVehicleModalOpen) {
      setIsVehicleModalOpen(true);
    }
  };

  const closeClientModal = () => {
    setVehicleUploadData(null);
    setAlarmInfo(null);
    setIsClientModalOpen(false);
  };

  const getArrowStyle = param => {
    if (vehicleUploadData?.engine_condition === 'healthy' && param === 1) {
      return true;
    } else if (vehicleUploadData?.engine_condition === 'unhealthy') {
      return true;
    }
  };

  console.log(vehicleUploadData, vehicleUploadData?.engine_condition);

  return (
    <div className={styles.pageBg}>
      <div className={styles.leftSection}>
        <div id={styles.vcdpModule} onClick={openVcdpModel}>
          VCDP
        </div>
        <ArrowRightOutlined
          id={styles.arrowBottomRightSvg}
          className={getArrowStyle(1) ? styles.arrow40Animation : null}
        />
        <div style={{ height: 120 }}>
          <SwapOutlined
            id={styles.arrowUpSvg}
            className={getArrowStyle(1) ? styles.arrow90Animation : null}
          />
        </div>
        <img id={styles.carModule} src={car} alt="car" onClick={openVehicleModel} />
      </div>
      <div className={styles.middleSection}>
        <div className={styles.VDPSMod}>
          <div id={styles.vdpsLabel}>VDPS</div>
          <div id={styles.model}>Machine Learning</div>
          <div style={{ height: 60 }}>
            <SwapOutlined
              id={styles.arrowSwapSvg}
              className={getArrowStyle(1) ? styles.arrow90Animation : null}
            />
          </div>
          <img id={styles.predictionModule} src={AI} alt="AI" />
        </div>
        <div style={{ height: 60 }}>
          <ArrowUpOutlined
            id={styles.arrowDownSvg}
            className={getArrowStyle(2) ? styles.arrow0Animation : null}
          />
        </div>
        <img id={styles.storeModule} src={store} alt="store" />
      </div>
      <div className={styles.rightSection}>
        <SwapOutlined
          id={styles.toClientArrow}
          className={getArrowStyle(2) ? styles.arrow0Animation : null}
        />
        <img
          className={alarmInfo ? styles.shakeAnimation : null}
          id={styles.iphoneModule}
          onClick={openClientModel}
          src={iphone}
          alt="iphone"
        />
      </div>
      <Modal
        width={'75%'}
        styles={{ body: { marginTop: 30, maxHeight: '650px', overflow: 'auto' } }}
        open={isVcdpModalOpen}
        onCancel={() => setIsVcdpModalOpen(false)}
        title={null}
        footer={[
          <Button
            key="submit"
            className={styles.closeBtn}
            onClick={() => setIsVcdpModalOpen(false)}
          >
            close
          </Button>
        ]}
      />
      <Modal
        width={'75%'}
        styles={{ body: { marginTop: 30, maxHeight: '650px', overflow: 'auto' } }}
        open={isClientModalOpen}
        onCancel={() => closeClientModal()}
        title={'client'}
        footer={[
          <Button key="submit" className={styles.closeBtn} onClick={() => closeClientModal()}>
            close
          </Button>
        ]}
      >
        <div>
          {vehicleUploadData?.engine_condition === 'unhealthy' ? (
            <Table columns={vehicleDColforShown} dataSource={[vehicleUploadData]} />
          ) : (
            <Skeleton active />
          )}
        </div>
      </Modal>
      <Modal
        width={'75%'}
        styles={{ body: { marginTop: 30, maxHeight: '650px', overflow: 'auto' } }}
        open={isVehicleModalOpen}
        onCancel={() => setIsVehicleModalOpen(false)}
        title={'vehicle'}
        footer={[
          <Button
            key="submit"
            className={styles.closeBtn}
            onClick={() => setIsVehicleModalOpen(false)}
          >
            close
          </Button>
        ]}
      >
        <div>
          <Table columns={vehicleDataCol} dataSource={vehicleData} />
        </div>
      </Modal>
    </div>
  );
};

export default PredictionSystem;
