#!/usr/bin/env node
/**
 * 小红书轮播图自动截图脚本
 * 使用 Puppeteer 截取 HTML 中的卡片并保存为图片
 */

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const OUTPUT_DIR = path.join(__dirname, '..', 'assets', 'xiaohongshu', '05-agent-team');
const HTML_FILE = path.join(__dirname, 'xiaohongshu-canvas-05.html');

// 确保输出目录存在
if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

async function screenshot() {
    console.log('🚀 启动浏览器...');

    const browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const page = await browser.newPage();
    await page.setViewport({ width: 1080, height: 1440 });

    // 读取 HTML 文件
    let htmlContent = fs.readFileSync(HTML_FILE, 'utf-8');

    // 隐藏下载按钮后再截图
    htmlContent = htmlContent.replace(
        '<div class="btn-container">',
        '<div class="btn-container" style="display: none;">'
    );

    await page.setContent(htmlContent, { waitUntil: 'networkidle0' });

    // 等待字体加载
    await new Promise(r => setTimeout(r, 2000));

    const cards = [
        { id: 'p1', name: '01-cover.png', desc: '封面' },
        { id: 'p2', name: '02-pain.png', desc: '痛点' },
        { id: 'p3', name: '03-architecture.png', desc: '架构' },
        { id: 'p4', name: '04-roles.png', desc: '角色' },
        { id: 'p5', name: '05-flow.png', desc: '流程' },
        { id: 'p6', name: '06-criteria.png', desc: '标准' }
    ];

    // 先删除旧的 p1-p9.png 文件
    for (let i = 1; i <= 9; i++) {
        const oldFile = path.join(OUTPUT_DIR, `p${i}.png`);
        if (fs.existsSync(oldFile)) {
            fs.unlinkSync(oldFile);
            console.log(`🗑️  删除旧文件：p${i}.png`);
        }
    }

    for (const card of cards) {
        console.log(`📸 正在截取 ${card.desc} (${card.name})...`);

        const element = await page.$(`#${card.id}`);
        if (element) {
            await element.screenshot({
                path: path.join(OUTPUT_DIR, card.name),
                type: 'png'
            });
            console.log(`   ✅ 已保存：${path.join(OUTPUT_DIR, card.name)}`);
        } else {
            console.log(`   ❌ 未找到元素：#${card.id}`);
        }

        // 滚动到下一个卡片
        await page.evaluate((id) => {
            const el = document.getElementById(id);
            if (el) el.scrollIntoView({ behavior: 'smooth' });
        }, card.id);
        await new Promise(r => setTimeout(r, 500));
    }

    await browser.close();
    console.log('\n✨ 全部截图完成！');
    console.log(`📁 输出目录：${OUTPUT_DIR}`);
}

screenshot().catch(console.error);
