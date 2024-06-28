import { useRef, useEffect } from 'react';

const useMount = () => {
  const mountRef = useRef(false);
  useEffect(() => {
    mountRef.current = true;
    return () => {
      mountRef.current = false;
    };
  }, []);
  return () => mountRef.current;
};

export { useMount };
