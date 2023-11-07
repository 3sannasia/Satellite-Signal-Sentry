import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react-swc";
import cesium from "vite-plugin-cesium";

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "");
  return {
    define: {
      "process.env.CESIUM_ACCESS_KEY": JSON.stringify(env.CESIUM_ACCESS_KEY),
    },
    plugins: [react(), cesium()],
  };
});
