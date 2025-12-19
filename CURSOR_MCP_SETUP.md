# 在 Cursor 中关联已注册的 MCP 服务器

本指南将帮助你在 Cursor IDE 中配置和关联已注册的 MCP（Model Context Protocol）服务器。

## 📋 前置要求

1. **安装 UV**（如果还没有安装）
   - Linux/macOS:
     ```bash
     curl -LsSf https://astral.sh/uv/install.sh | sh
     ```
   - Windows:
     ```powershell
     powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
     ```

2. **获取火山引擎凭证**
   - 从 [火山引擎控制台-访问控制](https://console.volcengine.com/iam/identitymanage/user) 获取 AccessKey 和 SecretKey
   - 确保这些凭证具有相应服务的权限

## 🔧 配置步骤

### 方法一：通过 Cursor 设置界面配置（推荐）

1. **打开 Cursor 设置**
   - 在 macOS 上：`Cursor` → `Settings` → `Features` → `Model Context Protocol`
   - 或使用快捷键 `Cmd + ,` 打开设置，然后搜索 "MCP"

2. **添加 MCP 服务器配置**
   - 在 MCP 设置中找到 "MCP Servers" 配置项
   - 点击 "Edit in Settings JSON" 或直接编辑配置文件

3. **配置文件位置**
   - macOS: `~/Library/Application Support/Cursor/User/globalStorage/mcp.json`
   - Windows: `%APPDATA%\Cursor\User\globalStorage\mcp.json`
   - Linux: `~/.config/Cursor/User/globalStorage/mcp.json`

### 方法二：直接编辑配置文件

1. **找到配置文件**
   - 按照上述路径找到 `mcp.json` 文件
   - 如果文件不存在，创建一个新文件

2. **添加 MCP 服务器配置**

   以 CDN MCP Server 为例，配置如下：

   ```json
   {
     "mcpServers": {
       "mcp-server-cdn": {
         "command": "uvx",
         "args": [
           "--from",
           "git+https://github.com/volcengine/mcp-server#subdirectory=server/mcp_server_cdn",
           "mcp_cdn"
         ],
         "env": {
           "VOLCENGINE_ACCESS_KEY": "你的AccessKey",
           "VOLCENGINE_SECRET_KEY": "你的SecretKey"
         }
       }
     }
   }
   ```

## 📝 配置多个 MCP 服务器

你可以在同一个配置文件中添加多个 MCP 服务器：

```json
{
  "mcpServers": {
    "mcp-server-cdn": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/volcengine/mcp-server#subdirectory=server/mcp_server_cdn",
        "mcp_cdn"
      ],
      "env": {
        "VOLCENGINE_ACCESS_KEY": "你的AccessKey",
        "VOLCENGINE_SECRET_KEY": "你的SecretKey"
      }
    },
    "mcp-server-ecs": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/volcengine/mcp-server#subdirectory=server/mcp_server_ecs",
        "mcp-server-ecs"
      ],
      "env": {
        "VOLCENGINE_ACCESS_KEY": "你的AccessKey",
        "VOLCENGINE_SECRET_KEY": "你的SecretKey",
        "VOLCENGINE_REGION": "cn-beijing"
      }
    },
    "mcp-server-tos": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/volcengine/mcp-server#subdirectory=server/mcp_server_tos",
        "mcp-server-tos"
      ],
      "env": {
        "VOLCENGINE_ACCESS_KEY": "你的AccessKey",
        "VOLCENGINE_SECRET_KEY": "你的SecretKey"
      }
    }
  }
}
```

## 🔄 使用本地源码运行（可选）

如果你已经克隆了仓库到本地，也可以使用本地路径运行：

```json
{
  "mcpServers": {
    "mcp-server-cdn": {
      "command": "uv",
      "args": [
        "--directory",
        "/绝对路径/mcp-server/server/mcp_server_cdn/src/CDN",
        "run",
        "mcp_server.py"
      ],
      "env": {
        "VOLCENGINE_ACCESS_KEY": "你的AccessKey",
        "VOLCENGINE_SECRET_KEY": "你的SecretKey"
      }
    }
  }
}
```

**注意**：使用本地路径时，请确保使用**绝对路径**。

## ✅ 验证配置

1. **重启 Cursor**
   - 保存配置文件后，重启 Cursor IDE

2. **检查 MCP 服务器状态**
   - 在 Cursor 的 MCP 设置界面中查看服务器状态
   - 如果配置正确，服务器应该显示为 "Connected" 或 "Running"

3. **测试功能**
   - 在 Cursor 的聊天界面中尝试使用 MCP 工具
   - 例如，对于 CDN MCP，可以尝试："查询我的 CDN 域名列表"

## 🐛 常见问题排查

### 1. MCP 服务器无法连接

- **检查 UV 是否已安装**
  ```bash
  uv --version
  ```

- **检查网络连接**
  - 确保可以访问 GitHub（如果使用 git+https 方式）

- **检查凭证是否正确**
  - 确认 AccessKey 和 SecretKey 是否正确填写
  - 确认凭证是否具有相应服务的权限

### 2. 配置文件格式错误

- **验证 JSON 格式**
  - 使用 JSON 验证工具检查配置文件格式
  - 确保所有引号、逗号、括号都正确匹配

### 3. 权限问题

- **检查文件权限**
  - 确保 Cursor 有权限读取配置文件
  - macOS/Linux: `chmod 644 mcp.json`

## 📚 更多资源

- [火山引擎 MCP 市场](https://www.volcengine.com/mcp-marketplace)
- [MCP 协议文档](https://modelcontextprotocol.io/introduction)
- [项目 GitHub 仓库](https://github.com/volcengine/mcp-server)

## 🔗 相关 MCP 服务器配置示例

### CDN MCP Server
```json
{
  "mcpServers": {
    "mcp-server-cdn": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/volcengine/mcp-server#subdirectory=server/mcp_server_cdn",
        "mcp_cdn"
      ],
      "env": {
        "VOLCENGINE_ACCESS_KEY": "你的AccessKey",
        "VOLCENGINE_SECRET_KEY": "你的SecretKey"
      }
    }
  }
}
```

### ECS MCP Server
```json
{
  "mcpServers": {
    "mcp-server-ecs": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/volcengine/mcp-server#subdirectory=server/mcp_server_ecs",
        "mcp-server-ecs"
      ],
      "env": {
        "VOLCENGINE_ACCESS_KEY": "你的AccessKey",
        "VOLCENGINE_SECRET_KEY": "你的SecretKey",
        "VOLCENGINE_REGION": "cn-beijing"
      }
    }
  }
}
```

### TOS MCP Server
```json
{
  "mcpServers": {
    "mcp-server-tos": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/volcengine/mcp-server#subdirectory=server/mcp_server_tos",
        "mcp-server-tos"
      ],
      "env": {
        "VOLCENGINE_ACCESS_KEY": "你的AccessKey",
        "VOLCENGINE_SECRET_KEY": "你的SecretKey"
      }
    }
  }
}
```

---

**提示**：每个 MCP 服务器可能有不同的环境变量要求，请参考对应服务器的 README 文档获取详细配置信息。

