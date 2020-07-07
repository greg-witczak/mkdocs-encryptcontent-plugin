# for NixOS: nix-shell for locally using the plugin

with import <nixpkgs> {};
with pkgs.python3Packages;

buildPythonPackage rec {
  name = "gw-mkdocs-encryptcontent-plugin";
  src = ./.;
  propagatedBuildInputs = [ ];
}
