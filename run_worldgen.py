# Example using the Python API
from worldgen import WorldGen
import torch
import open3d as o3d
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_path', type=str, default="./tmp/tmp", help='Path to save the output mesh')
    parser.add_argument('--prompt', type=str, default="a warm living room with a fireplace and large windows", help='Text prompt to generate the 3D world')
    parser.add_argument('--output_type', type=str, choices=['ply', 'glb', 'obj'], default="ply", help='Type of output to save')
    parser.add_argument('--device', type=str, default="cuda", help='Device to run the model on')
    args = parser.parse_args()
    
    device = torch.device(args.device if torch.cuda.is_available() else "cpu")

    worldgen = WorldGen(mode="t2s", device=device, low_vram=True) # Set low_vram to True if your GPU VRAM is less than 24GB.
    mesh = worldgen.generate_world(args.prompt, return_mesh=True)
    o3d.io.write_triangle_mesh(f"{args.output_path}.{args.output_type}", mesh)