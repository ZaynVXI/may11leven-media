import {Composition, AbsoluteFill, useCurrentFrame, interpolate, Easing} from 'remotion';
const Card = () => { const f = useCurrentFrame();
  const y = interpolate(f, [0, 30], [40, 0], {extrapolateRight: 'clamp', easing: Easing.bezier(.2,.7,.2,1)});
  const o = interpolate(f, [0, 24], [0, 1], {extrapolateRight: 'clamp'});
  return <AbsoluteFill style={{background:'#ECEAE4', justifyContent:'center', padding:96, fontFamily:'sans-serif'}}>
    <div style={{fontSize:28, letterSpacing:3, color:'#141213', fontFamily:'monospace'}}>MAY11LEVEN LABS</div>
    <div style={{fontSize:120, fontWeight:600, color:'#141213', transform:`translateY(${y}px)`, opacity:o, lineHeight:1}}>Seven services.<br/>One studio.</div>
  </AbsoluteFill>; };
export const Root = () => <Composition id="Card" component={Card} durationInFrames={60} fps={30} width={1080} height={1350}/>;
