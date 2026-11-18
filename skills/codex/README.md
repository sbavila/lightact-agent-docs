# LightAct skill

## Install

Run these commands from the root of your LightAct docs checkout. The link keeps the skill and its sources in the same checkout.

```sh
mkdir -p "$HOME/.agents/skills"
ln -s "$(pwd -P)/skills/codex/lightact" "$HOME/.agents/skills/lightact"
```

To install a copy, use the following commands instead. Both methods expect the destination to be unused.

```sh
mkdir -p "$HOME/.agents/skills"
cp -R skills/codex/lightact "$HOME/.agents/skills/lightact"
pwd -P > "$HOME/.agents/skills/lightact/checkout-path"
```

Keep the checkout. If you move it, recreate the link or update `checkout-path` with the new absolute path.
