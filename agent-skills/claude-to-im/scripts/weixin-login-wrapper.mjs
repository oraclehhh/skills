import { runWeixinLogin } from '../src/weixin-login.ts';

runWeixinLogin().catch((err) => {
  console.error('[weixin-login] Failed:', err instanceof Error ? err.message : String(err));
  process.exitCode = 1;
});
