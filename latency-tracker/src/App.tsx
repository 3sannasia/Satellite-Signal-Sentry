import { Viewer, Entity } from "resium";
import { Cartesian3, Color } from "cesium";
import { Ion } from "cesium";

Ion.defaultAccessToken =
  process.env.CESIUM_ACCESS_KEY || "Access Key Not Found";

console.log("Ion.defaultAccessToken", Ion.defaultAccessToken);
const position = Cartesian3.fromDegrees(-74.0707383, 40.7117244);
const pointGraphics = { pixelSize: 20, color: Color.RED };

function App() {
  return (
    <Viewer full>
      <Entity position={position} point={pointGraphics} />
    </Viewer>
  );
}

export default App;
