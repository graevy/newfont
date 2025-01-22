{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3Full
    pkgs.fontforge
    pkgs.python312Packages.pillow
  ];
}
